from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.decl())
        else:
            return self.visit(ctx.decl()) + self.visit(ctx.decls())
    
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visit(ctx.getChild(0))
    
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visit(ctx.getChild(0))
    
    def visitShortvardecl(self, ctx:MT22Parser.ShortvardeclContext):
        idlist = self.visit(ctx.idlist())
        vartype = self.visit(ctx.vartype())
        return [VarDecl(i,vartype) for i in idlist]
    
    
    def visitFulvardecl(self, ctx:MT22Parser.FulvardeclContext):
        if ctx.fulvardecl():
            next = self.visit(ctx.fulvardecl())
            ids = [ctx.ID().getText()] + [i.name for i in next]
            exprs = [i.init for i in next] + [self.visit(ctx.expr())]
            vartype = next[0].typ
            return [VarDecl(ids[i],vartype,exprs[i]) for i in range(len(ids))]
        
        return [VarDecl(ctx.ID().getText(),self.visit(ctx.vartype()),self.visit(ctx.expr()))]
    
    def visitArraydecl(self, ctx:MT22Parser.ArraydeclContext):
        intlitlist = self.visit(ctx.intlitlist())
        eletype = self.visit(ctx.eletype())
        return ArrayType(intlitlist, eletype)
    
    def visitEletype(self, ctx:MT22Parser.EletypeContext):
        return self.visit(ctx.atomictype())
    
    def visitVartype(self, ctx:MT22Parser.VartypeContext):
        if ctx.AUTOTYPE():
            return AutoType()
        return self.visit(ctx.getChild(0))
    
    def visitIntlitlist(self, ctx:MT22Parser.IntlitlistContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.intlitlist())

    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.getChildCount()==1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())

    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return [self.visit(ctx.expr())] if ctx.getChildCount()==1 else [self.visit(ctx.expr())] + self.visit(ctx.exprlist())
        
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        proto = self.visit(ctx.funcproto())
        body = self.visit(ctx.funcbody())
        return [FuncDecl(proto[0],proto[1],proto[2],proto[3],body)]
        
    def visitFuncproto(self, ctx:MT22Parser.FuncprotoContext):
        name = ctx.ID(0).getText()
        retype = self.visit(ctx.returntype())
        if ctx.paralistdecl():
            paradecl = self.visit(ctx.paralistdecl())
        else: paradecl = []
        if ctx.INHERIT(): 
            inher = ctx.ID(1)
        else:
            inher = None
        return [name,retype,paradecl,inher]
        
    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visit(ctx.blockstmt())
        
    def visitReturntype(self, ctx:MT22Parser.ReturntypeContext):
        if ctx.atomictype(): return self.visit(ctx.atomictype())
        elif ctx.arraydecl(): return self.visit(ctx.arraydecl())
        elif ctx.VOIDTYPE(): return VoidType()
        else: return AutoType()
        
    def visitParalistdecl(self, ctx:MT22Parser.ParalistdeclContext):
        return [self.visit(ctx.paradecl())]+self.visit(ctx.paralistdecl()) if ctx.paralistdecl() else [self.visit(ctx.paradecl())]
        
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        return ParamDecl(ctx.ID().getText(),self.visit(ctx.vartype()),True if ctx.OUT() else None,True if ctx.INHERIT() else None)
        
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visit(ctx.stringexpr())
        
    def visitStringexpr(self, ctx:MT22Parser.StringexprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.STRINGCONCAT().getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        
    def visitRelationalexpr(self, ctx:MT22Parser.RelationalexprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.RELATIONALOP().getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        
    def visitLogical_and_orexpr(self, ctx:MT22Parser.Logical_and_orexprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2))) 
        
    def visitAddingexpr(self, ctx:MT22Parser.AddingexprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))  
        
    def visitMultiplyingexpr(self, ctx:MT22Parser.MultiplyingexprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))  
        
    def visitLogical_negateexpr(self, ctx:MT22Parser.Logical_negateexprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return UnExpr(ctx.getChild(0).getText(),self.visit(ctx.getChild(1)))
        
    def visitSignexpr(self, ctx:MT22Parser.SignexprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return UnExpr(ctx.getChild(0).getText(),self.visit(ctx.getChild(1))) 
        
    def visitIndexopexpr(self, ctx:MT22Parser.IndexopexprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.indexop())
        
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visit(ctx.getChild(0))
        
    def visitBracket(self, ctx:MT22Parser.BracketContext):
        return self.visit(ctx.expr())
        
    def visitConst(self, ctx:MT22Parser.ConstContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        else: return BooleanLit((ctx.BOOLEANLIT().getText())=="true")
        
    def visitVar(self, ctx:MT22Parser.VarContext):
        return Id(ctx.ID().getText())
        
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        return FuncCall(ctx.ID().getText(),self.visit(ctx.arglist()))
        
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        return [self.visit(ctx.arg())] if ctx.getChildCount()==1 else [self.visit(ctx.arg())] + self.visit(arglist())
        
    def visitArg(self, ctx:MT22Parser.ArgContext):
        return self.visit(ctx.expr())
        
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist())) if ctx.exprlist() else ArrayLit([])
        
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))
        
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.lhs()),self.visit(ctx.expr()))
        
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        return self.visit(ctx.indexop())
        
    def visitIndexop(self, ctx:MT22Parser.IndexopContext):
        return ArrayCell(ctx.ID().getText(),self.visit(ctx.exprlist()))
        
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        if ctx.stmt(1): 
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)))
        
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return ForStmt(AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr(0))), self.visit(ctx.expr(1)),self.visit(ctx.expr(2)), self.visit(ctx.stmt()))
        
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()),self.visit(ctx.stmt()))
        
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        return DoWhileStmt(self.visit(ctx.expr()),self.visit(ctx.blockstmt()))
        
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return BreakStmt()
        
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return ContinueStmt()
        
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return ReturnStmt(self.visit(ctx.expr())) if ctx.expr() else ReturnStmt()
        
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        fc = self.visit(ctx.funccall())
        return CallStmt(fc.name,fc.args)
        
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        if ctx.blockBody():
            return BlockStmt(self.visit(ctx.blockBody()))
        return BlockStmt([])
        
    def visitBlockBody(self, ctx:MT22Parser.BlockBodyContext):
        if ctx.blockBody():
            return [self.visit(ctx.getChild(0))] + self.visit(ctx.blockBody())
        return [self.visit(ctx.getChild(0))]
        
    def visitAtomictype(self, ctx:MT22Parser.AtomictypeContext):
        if ctx.BOOLTYPE(): return BooleanType()
        if ctx.INTTYPE(): return IntegerType()
        if ctx.FLOATTYPE(): return FloatType()
        if ctx.STRINGTYPE(): return StringType()