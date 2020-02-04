// Derived from https://github.com/FAMILIAR-project/familiar-language/blob/master/org.xtext.example.fml.parent/org.xtext.example.fml/src/org/xtext/example/mydsl/Fml.xtext#L550
grammar fml;

featuremodel : ('FM'|'featuremodel') LEFT_PAREN ((FT_ID ';') | (production ';')+) (constraints ';')* RIGHT_PAREN ;

production  : FT_ID ':' child+ ;

child       : (mandatory
                | optional
                | xorgroup
                | orgroup  
               | mutexgroup ) ;
                

mandatory   : FT_ID ;
optional    : LEFT_HOOK FT_ID RIGHT_HOOK ;
xorgroup   : LEFT_PAREN FT_ID  (B_OR FT_ID)+ RIGHT_PAREN ;
orgroup    : LEFT_PAREN FT_ID  (B_OR FT_ID)+ RIGHT_PAREN PLUS ;


mutexgroup : LEFT_PAREN FT_ID  (B_OR FT_ID)+ ')?' ;

constraints :
      constraints '->' constraints
    | constraints '&' constraints
    | FT_ID
    | '(' constraints ')'      
    ; 

LCURLY : '{' ;

LEFT_HOOK : '[' ;
RIGHT_HOOK : ']' ;

LEFT_PAREN : '(' ;
RIGHT_PAREN : ')' ;

B_OR : '|' ;
PLUS : '+';

FT_ID : [a-zA-Z] [a-zA-Z0-9]* ;             // match upper/lower-case identifiers, numbers possible 

WS  :   [ \t\n\r]+ -> skip ;
