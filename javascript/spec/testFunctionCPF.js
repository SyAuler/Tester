
describe("Receber Dados", function(){

    describe("Validar CPF", function(){
        it("CPF Válido", function(){
            var retorno = TestaCPF("66278235005"); 
            expect(retorno).toEqual(true);
        });

        it("CPF Válido com pontuação", function(){
            var retorno = TestaCPF("010.884.949-00"); 
            expect(retorno).toEqual(false);
        });

        it("CPF número aleatório", function(){
            var retorno = TestaCPF("11110001111"); 
            expect(retorno).toEqual(false);
        });

        it("CPF Caracter", function(){
            var retorno = TestaCPF("cfg.vfg.sgh-sf"); 
            expect(retorno).toEqual(false);
        });
    });
});