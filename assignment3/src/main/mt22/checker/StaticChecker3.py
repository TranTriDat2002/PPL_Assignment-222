from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast, [])

    ##########Support function and global var#################

    loop_counter = 0

    def Infer(self, inferObj, typ, o):
        if type(inferObj) == FuncCall:
            for i in range(len(o)):
                if inferObj.name in o[i]:
                    o[i][inferObj.name].return_type = typ
                    break
        else:
            for i in range(len(o)):
                if inferObj.name in o[i]:
                    o[i][inferObj.name].typ = typ
                    break

    def Return_In_Statement(self, stmt, o):
        re_obj
        re_type
        if stmt.expr is None:
            re_type = VoidType()
        else:
            re_obj, re_type = self.visit(stmt.expr, o)

        nearest_func_name = list(o[-2].items())[-1][0]
        nearest_func_type = o[-2][nearest_func_name].return_type

        if type(re_type) == AutoType:
            self.Infer(re_obj, nearest_func_type, o)
        elif type(nearest_func_type) == AutoType:
            o[-2][nearest_func_name].return_type = re_type
        elif str(re_type) != str(nearest_func_type):
            if type(nearest_func_type) == FloatType and type(re_type) == IntegerType:
                pass
            elif type(nearest_func_type) == ArrayType and type(re_type) == ArrayType:
                if type(nearest_func_type.typ) == FloatType and type(re_type.typ) == IntegerType:
                    pass
                else:
                    raise TypeMismatchInExpression(stmt) 
            else:
                raise TypeMismatchInExpression(stmt)

    ##########################################################

    def visitProgram(self, ctx, o):
        # o = [{scope0}, {scope1},...]
        # o[scope] = {name0: object0, name1: object1,...}
        # o[scope][name] = Decl
        # Inner scope will append to head
        o = [{}]

        # Loop 1: Take function prototype (None -> not visited)
        for i in ctx.decls:
            if i.name in o[0]:
                if type(i) == FuncDecl:
                    raise Redeclared(Function(), i.name)
                elif type(i) == VarDecl:
                    raise Redeclared(Variable(), i.name)
            else:
                o[0][i.name] = i;
        
        if not "main" in o[0] or type(o[0]["main"].return_type) != VoidType or len(o[0]["main"].params) != 0:
            raise NoEntryPoint()

        # Get in 1 level => Level 0 for function prototypes but not declared. Level 1 for global
        o.insert(0,{})

        # Loop 2: Go through each Decl and check
        for i in ctx.decls:
            self.visit(i,o)
    
    def visitVarDecl(self,ctx,o):
        # (self, name: str, typ: Type, init: Expr or None = None)
        if str(ctx.name) in o[0]:
            raise Redeclared(Variable(), str(ctx.name))
        
        if ctx.init is None:
            if type(ctx.typ) == AutoType:
                raise Invalid(Variable(), str(ctx.name))
            else:
                o[0][str(ctx.name)] = ctx

        else:
            # If a:integer = a; => Valid????????????????????????????????????????????????
            if type(ctx.init) == Id and str(ctx.init.name) == str(ctx.name):
                o[0][str(ctx.name)] = ctx
            else:

                initObject, initType = self.visit(ctx.init, o)
                if type(ctx.typ) == AutoType:            
                    ctx.typ = initType
                    o[0][str(ctx.name)] = ctx
                
                elif type(initType) == AutoType: #Function and para can have autotype => visit may return Id or FuncCall
                    self.Infer(initObject, ctx.typ, o)
                        
                    
                elif str(initType) != str(ctx.typ):
                    
                    if type(initType) == IntegerType and type(ctx.typ) == FloatType:
                        o[0][str(ctx.name)] = ctx
                    elif type(initType) == ArrayType and type(ctx.typ) == ArrayType:
                        if type(ctx.typ.typ) == FloatType and type(initType.typ) == IntegerType:
                            o[0][str(ctx.name)] = ctx
                        else:
                            raise TypeMismatchInVarDecl(ctx) 
                    else:
                        raise TypeMismatchInVarDecl(ctx)
                else:
                    o[0][str(ctx.name)] = ctx
    
    def visitFuncDecl(self,ctx,o):
        #(self, name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt)

        # Support var
        parent_inherit_para = {}
        parent_function = {} # Store super or preventDefault

        if ctx.inherit is not None:
            # Check first stmt in body

            # No super (Nothing or not CallStmt or CallStmt not super and preventDefault)
            if len(ctx.body.body) == 0 or type(ctx.body.body[0]) != CallStmt or (ctx.body.body[0].name != "super" and ctx.body.body[0].name != "preventDefault"):
                
                # Check if parent exist
                i = o[-1]
                if str(ctx.inherit) in i and type(i[str(ctx.inherit)]) == FuncDecl: 

                    # Parent have para
                    if len(i[str(ctx.inherit)].params) > 0:
                        raise InvalidStatementInFunction(str(ctx.name))
            
                    # Parent have no para => Implicit call (But have no para and name existed -> skip)

                    # Check if parent is also inherit
                    ancestor = i[str(ctx.inherit)]
                    while ancestor.inherit is not None:
                        if str(ancestor.inherit) in o[-1]:
                            # Check parent paras
                            check_para_tmp = []
                            for j in i[str(ancestor.inherit)].params:
                                if j.name in check_para_tmp:
                                    raise Redeclared(Parameter(), j.name)
                                else:
                                    check_para_tmp.append(j.name)
                                    
                                # Take inherit
                                if j.inherit:
                                    if j.name in parent_inherit_para:
                                        raise Invalid(Parameter(), j.name)
                                    parent_inherit_para[j.name] = j
                        else:
                            raise Undeclared(Function(), ancestor.inherit)
                        ancestor = i[str(ancestor.inherit)]

                    # Add super and preventDefault
                    parentFunc = i[str(ctx.inherit)]
                    parent_function["super"] = FuncDecl("super", parentFunc.return_type, parentFunc.params, parentFunc.inherit, parentFunc.body)
                    parent_function["preventDefault"] = FuncDecl("preventDefault", VoidType(), [], None, BlockStmt([]))


                # Parent not exist
                else:
                    raise Undeclared(Function(), ctx.inherit)
  
            # First Stmt is Super
            elif ctx.body.body[0].name == "super":

                # Check if parent exist
                i = o[-1]
                if str(ctx.inherit) in i and type(i[str(ctx.inherit)]) == FuncDecl: 
                    
                    # Check parent paras
                    check_para_tmp = []
                    for j in i[str(ctx.inherit)].params:
                        if j.name in check_para_tmp:
                            raise Redeclared(Parameter(), j.name)
                        else:
                            check_para_tmp.append(j.name)

                    # Compare params - super args
                    para = i[str(ctx.inherit)].params
                    arg = ctx.body.body[0].args

                    # Check para-arg length
                    if len(para) > len(arg):
                        raise TypeMismatchInExpression("")
                    if len(para) < len(arg):
                        raise TypeMismatchInExpression(arg[len(para)])
                    
                    # Check para type - arg type
                    for j in range(len(para)):
                        
                        arg, argtype = self.visit(arg[j],o)
                        paratype = para[j].typ

                        if type(argtype) == AutoType: # Function and para
                            self.Infer(arg, paratype, o) 

                        elif type(paratype) == AutoType:
                            i[ctx.str].params[j].typ = argtype
                        elif str(paratype) != str(argtype):
                            if type(argtype) == IntegerType and type(paratype) == FloatType:
                                pass
                            elif type(argtype) == ArrayType and type(paratype) == ArrayType:
                                if type(paratype.typ) == FloatType and type(argtype.typ) == IntegerType:
                                    pass
                                else:
                                    raise TypeMismatchInExpression(arg)
                            else:
                                raise  TypeMismatchInExpression(arg)
                    
                    # Check if parent is also inherit
                    ancestor = i[str(ctx.inherit)]
                    # print("Ancestor type: ", ancestor)
                    while ancestor.inherit is not None:
                        if str(ancestor.inherit) in o[-1]:
                            # Check parent paras
                            check_para_tmp = []
                            for j in i[str(ancestor.inherit)].params:
                                if j.name in check_para_tmp:
                                    raise Redeclared(Parameter(), j.name)
                                else:
                                    check_para_tmp.append(j.name)
                                    
                                # Take inherit
                                if j.inherit:
                                    if j.name in parent_inherit_para:
                                        raise Invalid(Parameter(), j.name)
                                    parent_inherit_para[j.name] = j
                        else:
                            raise Undeclared(Function(), ancestor.inherit)
                        ancestor = i[str(ancestor.inherit)]
                    
                    # Add super and preventDefault
                    parentFunc = i[str(ctx.inherit)]
                    parent_function["super"] = FuncDecl("super", parentFunc.return_type, parentFunc.params, parentFunc.inherit, parentFunc.body)
                    parent_function["preventDefault"] = FuncDecl("preventDefault", VoidType(), [], None, BlockStmt([]))
                
                # Parent not exist
                else:
                    raise Undeclared(Function(), ctx.inherit)
                
            # First Stmt is PD
            elif ctx.body.body[0].name == "preventDefault":
                # Add pv only
                parent_function["preventDefault"] = FuncDecl("preventDefault", VoidType(), [], None, BlockStmt([]))

        # Inherit is none
        else:
            pass
        
        # Check redeclared para first
        check_para_tmp = {}
        for i in ctx.params:
            if i.name in check_para_tmp:
                raise Redeclared(Parameter(), i.name)
            else:
                check_para_tmp[i.name] = i

        # Check all params
        para_and_function = {**parent_inherit_para, **parent_function}
        o.insert(0, para_and_function)
        for i in check_para_tmp:
            if i in o[0]:
                raise Invalid(Parameter(), check_para_tmp[i].name)
            else:
                o[0][i] = check_para_tmp[i]
        
        # Add fundecl to declarations
        
        o[-2][str(ctx.name)] = o[-1][str(ctx.name)]

        # Check body (blockstmt)

        returned = False

        for i in ctx.body.body:
            if type(i) == ReturnStmt:
                if not returned:
                    # (self, expr: Expr or None = None)
                    re_obj = None
                    re_type = None
                    if i.expr is None:
                        re_type = VoidType()
                    else:
                        re_obj, re_type = self.visit(i.expr, o)
                    if type(re_type) == AutoType:
                        self.Infer(re_obj, ctx.return_type, o)
                    elif type(ctx.return_type) == AutoType:
                        o[-2][str(ctx.name)].return_type = re_type
                    elif str(re_type) != str(ctx.return_type):
                        if type(ctx.return_type) == FloatType and type(re_type) == IntegerType:
                            pass
                        elif type(ctx.return_type) == ArrayType and type(re_type) == ArrayType:
                            if type(ctx.return_type.typ) == FloatType and type(re_type.typ) == IntegerType:
                                pass
                            else:
                                raise TypeMismatchInExpression(i)
                        else:
                            raise TypeMismatchInExpression(i)
                    returned = True
            else:
                self.visit(i, o)

        o.pop(0)
        
    def visitParamDecl(self,ctx,o):
        # (self, name: str, typ: Type, out: bool = False, inherit: bool = False)
        pass

    def visitId(self,ctx,o):
        # (self, name: str)
        for i in o[:-1]:
            if str(ctx.name) in i:
                if type(i[str(ctx.name)]) == VarDecl or type(i[str(ctx.name)]) ==ParamDecl:
                    return ctx, i[str(ctx.name)].typ
                else:
                    raise TypeMismatchInExpression(ctx)
        else:
            raise Undeclared(Identifier(), str(ctx.name))
            
    def visitArrayCell(self, ctx, o):
        # (self, name: str, cell: List[Expr])
        for i in o[:-1]:
            if str(ctx.name) in i:
                check_obj = i[str(ctx.name)]
                if type(check_obj) == VarDecl or type(check_obj) == ParamDecl:
                    if type(check_obj.typ) == ArrayType:
                        # (self, dimensions: List[int], typ: AtomicType)
                        # Check len of cell
                        if len(ctx.cell) > len(check_obj.typ.dimensions):
                            raise TypeMismatchInExpression(ctx)
                        else:
                            # Check cell expr types
                            for j in ctx.cell:
                                expr_obj, expr_type = self.visit(j,o)
                                if type(expr_type) == IntegerType:
                                    pass
                                elif type(expr_type) == AutoType: # Function or para
                                    # Infer
                                    self.Infer(expr_obj, IntegerType(), o)
                                else:
                                    raise TypeMismatchInExpression(ctx)
                            # Check dimensions and return
                            remain_dims = len(check_obj.typ.dimensions) - len(ctx.cell)
                            if remain_dims == 0:
                                return ctx, check_obj.typ.typ
                            else:
                                return ctx, ArrayType(check_obj.typ.dimensions[-remain_dims:],check_obj.typ.typ)
                    else: # Auto is also not allowed
                        raise TypeMismatchInExpression(ctx)

                else:
                    raise TypeMismatchInExpression(ctx)
        else:
            raise Undeclared(Identifier(), str(ctx.name))

    def visitBinExpr(self, ctx, o):
        # (self, op: str, left: Expr, right: Expr)
        
        # Check exprs
        left_obj, left_type = self.visit(ctx.left, o)
        right_obj, right_type = self.visit(ctx.right, o)

        # Classify operators
        if ctx.op in ["-", "+", "*", "/"]:
            if type(left_type) not in [IntegerType, FloatType, AutoType] or type(right_type) not in [IntegerType, FloatType, AutoType]:
                raise TypeMismatchInExpression(ctx)
            elif type(left_type) == AutoType and type(right_type) == AutoType:
                self.Infer(left_obj, IntegerType(), o)
                self.Infer(right_obj, IntegerType(), o)
                return ctx, IntegerType()
            elif type(left_type) == AutoType:
                self.Infer(left_obj, right_type, o)
                return ctx, right_type
            elif type(right_type) == AutoType:
                self.Infer(right_obj, left_type, o)
                return ctx, left_type
            else:
                if type(left_type) == FloatType or type(right_type) == FloatType:
                    return ctx, FloatType()
                return ctx, IntegerType()

        elif ctx.op in ["&&", "||"]:
            if type(left_type) not in [BooleanType, AutoType] or type(right_type) not in [BooleanType, AutoType]:
                raise TypeMismatchInExpression(ctx)
            if type(left_type) == AutoType:
                self.Infer(left_obj, BooleanType(), o)
            if type(right_type) == AutoType:
                self.Infer(right_obj, BooleanType(), o)
            return ctx, BooleanType()

        elif ctx.op == "::":
            if type(left_type) not in [StringType, AutoType] or type(right_type) not in [StringType, AutoType]:
                raise TypeMismatchInExpression(ctx)
            if type(left_type) == AutoType:
                self.Infer(left_obj, StringType(), o)
            if type(right_type) == AutoType:
                self.Infer(right_obj, StringType(), o)
            return ctx, StringType()
        
        elif ctx.op in ["==", "!="]:
            if type(left_type) not in [IntegerType, BooleanType, AutoType] or type(right_type) not in [IntegerType, BooleanType, AutoType]:
                raise TypeMismatchInExpression(ctx)
            elif type(left_type) == AutoType:
                self.Infer(left_obj, right_type, o)
            elif type(right_type) == AutoType:
                self.Infer(right_obj, left_type, o)
            return ctx, BooleanType()
        
        elif ctx.op in ["<", ">", "<=", ">="]:
            if type(left_type) not in [IntegerType, FloatType, AutoType] or type(right_type) not in [IntegerType, FloatType, AutoType]:
                raise TypeMismatchInExpression(ctx)
            elif type(left_type) == AutoType and type(right_type) == AutoType:
                self.Infer(left_obj, IntegerType(), o)
                self.Infer(right_obj, IntegerType(), o)
            elif type(left_type) == AutoType:
                self.Infer(left_obj, right_type, o)
            elif type(right_type) == AutoType:
                self.Infer(right_obj, left_type, o)
            return ctx, BooleanType()
        
        elif ctx.op == "%":
            if type(left_type) not in [IntegerType, AutoType] or type(right_type) not in [IntegerType, AutoType]:
                raise TypeMismatchInExpression(ctx)
            if type(left_type) == AutoType:
                self.Infer(left_obj, IntegerType(), o)
            if type(right_type) == AutoType:
                self.Infer(right_obj, IntegerType(), o)
            return ctx, IntegerType()

    def visitUnExpr(self, ctx, o):
        # (self, op: str, val: Expr)
        expr_obj, expr_type = self.visit(ctx.val, o)

        if ctx.op == "!":
            if type(expr_type) not in [BooleanType, AutoType]:
                raise TypeMismatchInExpression(ctx)
            elif type(expr_type) == AutoType:
                self.Infer(expr_obj, BooleanType(), o)
            return ctx, BooleanType()
        
        elif ctx.op == "-":
            if type(expr_type) not in [IntegerType, FloatType, AutoType]:
                raise TypeMismatchInExpression(ctx)
            elif type(expr_type) == AutoType:
                self.Infer(expr_obj, IntegerType(), o)
                return ctx, IntegerType()
            else:
                return ctx, expr_type

    def visitIntegerLit(self, ctx, o):
        return ctx, IntegerType()
    
    def visitFloatLit(self, ctx, o):
        return ctx, FloatType()
    
    def visitStringLit(self, ctx, o):
        return ctx, StringType()
    
    def visitBooleanLit(self, ctx, o):
        return ctx, BooleanType()

    def visitArrayLit(self, ctx, o):
        # (self, explist: List[Expr])

        exprs_type = []
        for i in ctx.explist:
            expr_obj, expr_type = self.visit(i,o)
            exprs_type.append(expr_type)

        litType = exprs_type[0]
        for i in exprs_type:
            if str(i) != str(litType):
                if type(i) == FloatType and type(litType) == IntegerType:
                    litType = FloatType()
                elif type(litType) == FloatType and type(i) == IntegerType:
                    pass
                elif type(i) == ArrayType and type(litType) == ArrayType:
                    # print("Comparing: ", i.dimensions, " with ",litType.dimensions)
                    if i.dimensions == litType.dimensions:
                        if type(i.typ) == FloatType and type(litType.typ) == IntegerType:
                            litType = ArrayType(litType.dimensions, FloatType())
                        elif type(i.typ) == IntegerType and type(litType.typ) == FloatType:
                            pass
                        else:
                            raise IllegalArrayLiteral(ctx)
                    else:
                        raise IllegalArrayLiteral(ctx)
                else:
                    raise IllegalArrayLiteral(ctx)
            # print("Got ", litType)
        if type(litType) in [IntegerType, FloatType, BooleanType, StringType]:
            # print("Got: ", [len(exprs_type)], " of ",litType )
            return ctx, ArrayType([len(exprs_type)],litType)
        else:
            predims = litType.dimensions
            # print("Got: ", [len(exprs_type)]+predims, "of", litType.typ )
            # print("Got final ", ArrayType([len(exprs_type)]+predims,litType.typ))
            return ctx, ArrayType([len(exprs_type)]+predims,litType.typ)

    def visitFuncCall(self, ctx, o):
        # (self, name: str, args: List[Expr])

        # If name is a special name
        if str(ctx.name) in ["readInteger","readBoolean","readFloat","readString"]:
            if len(args) != 0:
                raise TypeMismatchInExpression(ctx)
            if str(ctx.name) == "readInteger":
                return ctx, IntegerType()
            if str(ctx.name) == "readBoolean":
                return ctx, BooleanType()
            if str(ctx.name) == "readFloat":
                return ctx, FloatType()
            if str(ctx.name) == "readString":
                return ctx, StringType()
            
        elif str(ctx.name) in ["printInteger","writeFloat","printBoolean","printString"]:
            raise TypeMismatchInExpression(ctx)

        else:
            for i in o:
                if str(ctx.name) in i:
                    if type(i[str(ctx.name)]) == FuncDecl:
                        callee = i[str(ctx.name)]

                        # Check function para if not being declared?????##################################################

                        # Check return type
                        if type(callee.return_type) == VoidType:
                            raise TypeMismatchInExpression(ctx)
                        
                        # Check para-arg
                        params = callee.params
                        args = ctx.args

                        if len(args) != len(params):
                            raise TypeMismatchInExpression(ctx)

                        for j in range(len(params)):
                            arg_obj, args_type = self.visit(args[j],o)
                            paratype = params[j].typ

                            if type(args_type) == AutoType:
                                self.Infer(arg_obj, paratype, o) 

                            elif type(paratype) == AutoType:
                                self.Infer(params[j], args_type, o)

                            elif str(paratype) != str(args_type):
                                if type(args_type) == IntegerType and type(paratype) == FloatType:
                                    pass
                                elif type(args_type) == ArrayType and type(paratype) == ArrayType:
                                    if type(paratype.typ) == FloatType and type(args_type.typ) == IntegerType:
                                        pass
                                    else:
                                        raise TypeMismatchInExpression(ctx)
                                else:
                                    raise  TypeMismatchInExpression(ctx)
                        
                        return ctx, callee.return_type
                    else:
                        raise TypeMismatchInExpression(ctx)

                    break    

            else:
                raise Undeclared(Function(), str(ctx.name))
    
    def visitAssignStmt(self, ctx, o):
        # (self, lhs: LHS, rhs: Expr)

        lhs_obj, lhs_type = self.visit(ctx.lhs, o)
        rhs_obj, rhs_type = self.visit(ctx.rhs, o)

        # Check lhs
        if type(lhs_type) == VoidType or type(lhs_type) == ArrayType:
            raise TypeMismatchInStatement(ctx)
        
        # Check lhs-rhs
        if type(lhs_type) == AutoType:
            self.Infer(lhs_obj, rhs_obj, o)
        elif type(rhs_type) == AutoType:
            self.Infer(rhs_obj, lhs_type, o)
        elif str(lhs_type) != str(rhs_type):
            if type(lhs_type) == FloatType and type(rhs_type) == IntegerType:
                pass
            elif type(lhs_type) == ArrayType and type(rhs_type) == ArrayType:
                if type(lhs_type.typ) == FloatType and type(rhs_type.typ) == IntegerType:
                    pass
                else:
                    raise TypeMismatchInStatement(ctx)
            else:
                raise TypeMismatchInStatement(ctx)
        
    def visitBlockStmt(self, ctx, o):
        # (self, body: List[Stmt or VarDecl])
        for i in ctx.body:

            if type(i) == ReturnStmt:
                # (self, expr: Expr or None = None)
                re_obj = None
                re_type = None
                if i.expr is None:
                    re_type = VoidType()
                else:
                    re_obj, re_type = self.visit(i.expr, o)

                nearest_func_name = list(o[-2].items())[-1][0]
                nearest_func_type = o[-2][nearest_func_name].return_type

                if type(re_type) == AutoType:
                    self.Infer(re_obj, nearest_func_type, o)
                elif type(nearest_func_type) == AutoType:
                    o[-2][nearest_func_name].return_type = re_type
                elif str(re_type) != str(nearest_func_type):
                    if type(nearest_func_type) == FloatType and type(re_type) == IntegerType:
                        pass
                    elif type(nearest_func_type) == ArrayType and type(re_type) == ArrayType:
                        if type(nearest_func_type.typ) == FloatType and type(re_type.typ) == IntegerType:
                            pass
                        else:
                            raise TypeMismatchInExpression(i)
                    else:
                        raise TypeMismatchInExpression(i)

            elif type(i) == BlockStmt:
                o.insert(0,{})
                self.visit(i,o)
                o.pop(0)
            else:
                self.visit(i,o)
    
    def visitIfStmt(self, ctx, o):
        # (self, cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None)
        cond_obj, cond_type = self.visit(ctx.cond, o)
        if type(cond_type) == AutoType:
            self.Infer(cond_obj, BooleanType(), o)
        elif type(cond_type) != BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        if type(ctx.tstmt) == ReturnStmt:
            try:
                self.Return_In_Statement(ctx.tstm, o)
            except:
                raise
        elif type(ctx.tstmt) == BlockStmt:
            o.insert(0,{})
            self.visit(ctx.tstmt,o)
            o.pop(0)
        else:
            self.visit(ctx.tstmt,o)

        if type(ctx.fstmt) == ReturnStmt:
            try:
                self.Return_In_Statement(ctx.fstm, o)
            except:
                raise
        elif type(ctx.fstmt) == BlockStmt:
            o.insert(0,{})
            self.visit(ctx.fstmt,o)
            o.pop(0)
        else:
            self.visit(ctx.fstmt,o) 

    def visitForStmt(self, ctx, o):
        # (self, init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt)

        # Test init
        try:
            self.visit(ctx.init, o)
        except TypeMismatchInStatement:
            raise TypeMismatchInStatement(ctx)
        except:
            raise

        init_lhs_obj, init_lhs_type = self.visit(ctx.init.lhs, o)
        init_rhs_obj, init_rhs_type = self.visit(ctx.init.rhs, o)

        if type(init_lhs_type) == AutoType and type(init_rhs_type) == AutoType:
            self.Infer(init_lhs_obj, IntegerType(), o)
            self.Infer(init_rhs_obj, IntegerType(), o)
        elif type(init_lhs_type) != IntegerType:
            raise TypeMismatchInStatement(ctx)
        
        # Test cond
        cond_obj, cond_type = self.visit(ctx.cond, o)
        if type(cond_type) == AutoType:
            self.Infer(cond_obj, BooleanType(), o)
        elif type(cond_type) != BooleanType:
            raise TypeMismatchInStatement(ctx)

        # Test update expression
        udp_obj, upd_type = self.visit(ctx.upd, o)
        if type(upd_type) != IntegerType:
            if type(upd_type) == AutoType:
                self.Infer(udp_obj, IntegerType(), o)
            else:
                raise TypeMismatchInStatement(ctx)
        
        # Statement
        loop_counter = loop_counter + 1

        if type(ctx.stmt) == ReturnStmt:
            try:
                self.Return_In_Statement(ctx.stm, o)
            except:
                raise
        elif type(ctx.stmt) == BlockStmt:
            o.insert(0,{})
            self.visit(ctx.stmt,o)
            o.pop(0)
        else:
            self.visit(ctx.stmt,o)
        
        loop_counter = loop_counter - 1

    def visitWhileStmt(self, ctx, o):
        # (self, cond: Expr, stmt: Stmt)
        cond_obj, cond_type = self.visit(ctx.cond, o)
        if type(cond_type) == AutoType:
            self.Infer(cond_obj, BooleanType(), o)
        elif type(cond_type) != BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        loop_counter = loop_counter + 1

        if type(ctx.stmt) == ReturnStmt:
            try:
                self.Return_In_Statement(ctx.stm, o)
            except:
                raise
        elif type(ctx.stmt) == BlockStmt:
            o.insert(0,{})
            self.visit(ctx.stmt,o)
            o.pop(0)
        else:
            self.visit(ctx.stmt,o)

        loop_counter = loop_counter - 1

    def visitDoWhileStmt(self, ctx, o):
        # (self, cond: Expr, stmt: BlockStmt)
        cond_obj, cond_type = self.visit(ctx.cond, o)
        if type(cond_type) == AutoType:
            self.Infer(cond_obj, BooleanType(), o)
        elif type(cond_type) != BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        loop_counter = loop_counter + 1

        o.insert(0,{})
        self.visit(ctx.stmt,o)
        o.pop(0)

        loop_counter = loop_counter - 1

    def visitBreakStmt(self, ctx, o):
        if loop_counter == 0:
            raise MustInLoop(ctx)

    def visitContinueStmt(self, ctx, o):
        if loop_counter == 0:
            raise MustInLoop(ctx)

    def visitReturnStmt(self, ctx, o):
        # (self, expr: Expr or None = None)
        pass

    def visitCallStmt(self, ctx, o):
        # (self, name: str, args: List[Expr])

        # If name is a special name
        if str(ctx.name) in ["readInteger","readBoolean","readFloat","readString"]:
            if len(args) != 0:
                raise TypeMismatchInStatement(ctx)
            
        elif str(ctx.name) in ["printInteger","writeFloat","printBoolean","printString"]:
            if len(args) != 1:
                raise TypeMismatchInStatement(ctx)

        else:
            for i in o:
                # print("Finding: ", str(ctx.name))
                if str(ctx.name) in i:
                    # print("Found: ", str(ctx.name))
                    if type(i[str(ctx.name)]) == FuncDecl:
                        callee = i[str(ctx.name)]

                        # Check function para if not being declared?????##################################################

                        # Check para-arg
                        params = callee.params
                        args = ctx.args

                        if len(args) != len(params):
                            raise TypeMismatchInStatement(ctx)

                        for j in range(len(params)):
                            arg_obj, args_type = self.visit(args[j],o)
                            paratype = params[j].typ

                            if type(args_type) == AutoType:
                                self.Infer(arg_obj, paratype, o) 

                            elif type(paratype) == AutoType:
                                self.Infer(params[j], args_type, o)

                            elif str(paratype) != str(args_type):
                                if type(args_type) == IntegerType and type(paratype) == FloatType:
                                    pass
                                elif type(args_type) == ArrayType and type(paratype) == ArrayType:
                                    if type(paratype.typ) == FloatType and type(args_type.typ) == IntegerType:
                                        pass
                                    else:
                                        raise TypeMismatchInStatement(ctx)
                                else:
                                    raise  TypeMismatchInStatement(ctx)

                    else:
                        raise TypeMismatchInExpression(ctx)

                    break    

            else:
                raise Undeclared(Function(), str(ctx.name))
    