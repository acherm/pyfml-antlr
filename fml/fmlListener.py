# Generated from fml.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fmlParser import fmlParser
else:
    from fmlParser import fmlParser

# This class defines a complete listener for a parse tree produced by fmlParser.
class fmlListener(ParseTreeListener):

    # Enter a parse tree produced by fmlParser#featuremodel.
    def enterFeaturemodel(self, ctx:fmlParser.FeaturemodelContext):
        pass

    # Exit a parse tree produced by fmlParser#featuremodel.
    def exitFeaturemodel(self, ctx:fmlParser.FeaturemodelContext):
        pass


    # Enter a parse tree produced by fmlParser#production.
    def enterProduction(self, ctx:fmlParser.ProductionContext):
        pass

    # Exit a parse tree produced by fmlParser#production.
    def exitProduction(self, ctx:fmlParser.ProductionContext):
        pass


    # Enter a parse tree produced by fmlParser#child.
    def enterChild(self, ctx:fmlParser.ChildContext):
        pass

    # Exit a parse tree produced by fmlParser#child.
    def exitChild(self, ctx:fmlParser.ChildContext):
        pass


    # Enter a parse tree produced by fmlParser#mandatory.
    def enterMandatory(self, ctx:fmlParser.MandatoryContext):
        pass

    # Exit a parse tree produced by fmlParser#mandatory.
    def exitMandatory(self, ctx:fmlParser.MandatoryContext):
        pass


    # Enter a parse tree produced by fmlParser#optional.
    def enterOptional(self, ctx:fmlParser.OptionalContext):
        pass

    # Exit a parse tree produced by fmlParser#optional.
    def exitOptional(self, ctx:fmlParser.OptionalContext):
        pass


    # Enter a parse tree produced by fmlParser#xorgroup.
    def enterXorgroup(self, ctx:fmlParser.XorgroupContext):
        pass

    # Exit a parse tree produced by fmlParser#xorgroup.
    def exitXorgroup(self, ctx:fmlParser.XorgroupContext):
        pass


    # Enter a parse tree produced by fmlParser#orgroup.
    def enterOrgroup(self, ctx:fmlParser.OrgroupContext):
        pass

    # Exit a parse tree produced by fmlParser#orgroup.
    def exitOrgroup(self, ctx:fmlParser.OrgroupContext):
        pass


    # Enter a parse tree produced by fmlParser#mutexgroup.
    def enterMutexgroup(self, ctx:fmlParser.MutexgroupContext):
        pass

    # Exit a parse tree produced by fmlParser#mutexgroup.
    def exitMutexgroup(self, ctx:fmlParser.MutexgroupContext):
        pass


    # Enter a parse tree produced by fmlParser#constraints.
    def enterConstraints(self, ctx:fmlParser.ConstraintsContext):
        pass

    # Exit a parse tree produced by fmlParser#constraints.
    def exitConstraints(self, ctx:fmlParser.ConstraintsContext):
        pass


