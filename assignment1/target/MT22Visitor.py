# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#shortvardecl.
    def visitShortvardecl(self, ctx:MT22Parser.ShortvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fulvardecl.
    def visitFulvardecl(self, ctx:MT22Parser.FulvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraydecl.
    def visitArraydecl(self, ctx:MT22Parser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#eletype.
    def visitEletype(self, ctx:MT22Parser.EletypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vartype.
    def visitVartype(self, ctx:MT22Parser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlitlist.
    def visitIntlitlist(self, ctx:MT22Parser.IntlitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcproto.
    def visitFuncproto(self, ctx:MT22Parser.FuncprotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcbody.
    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returntype.
    def visitReturntype(self, ctx:MT22Parser.ReturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paralistdecl.
    def visitParalistdecl(self, ctx:MT22Parser.ParalistdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paradecl.
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringexpr.
    def visitStringexpr(self, ctx:MT22Parser.StringexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalexpr.
    def visitRelationalexpr(self, ctx:MT22Parser.RelationalexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_and_orexpr.
    def visitLogical_and_orexpr(self, ctx:MT22Parser.Logical_and_orexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#addingexpr.
    def visitAddingexpr(self, ctx:MT22Parser.AddingexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplyingexpr.
    def visitMultiplyingexpr(self, ctx:MT22Parser.MultiplyingexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_negateexpr.
    def visitLogical_negateexpr(self, ctx:MT22Parser.Logical_negateexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#signexpr.
    def visitSignexpr(self, ctx:MT22Parser.SignexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexopexpr.
    def visitIndexopexpr(self, ctx:MT22Parser.IndexopexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bracket.
    def visitBracket(self, ctx:MT22Parser.BracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#const.
    def visitConst(self, ctx:MT22Parser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var.
    def visitVar(self, ctx:MT22Parser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funccall.
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arglist.
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arg.
    def visitArg(self, ctx:MT22Parser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexop.
    def visitIndexop(self, ctx:MT22Parser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockBody.
    def visitBlockBody(self, ctx:MT22Parser.BlockBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomictype.
    def visitAtomictype(self, ctx:MT22Parser.AtomictypeContext):
        return self.visitChildren(ctx)



del MT22Parser