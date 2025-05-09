import pytest
from enc_dec import encrypt
from freq_dist import freq_dist_attack

@pytest.mark.parametrize("texto_original, chave_correta", [
    ("viajarparapraiasdocalor", "aaaa"),
    ("amanhateremosreuniaoimportante", "aaaaaaa"),
    ("cafecomleiteehmeubebidafavorita", "aaaaaaaaaa"),
    ("jogosolimpicossaoemocionantes", "aaa"),
    ("chuvasdeveraoenchemasruas", "aaa"),
    ("compreiosingredientesdopudim", "aaaaaa"),
    ("festadeaniversariofoiumsucesso", "aaaaaaaaaaa"),
    ("pratiqueesportesparavivermais", "aaaaaaaaaaaaaaaaa"),
    ("mercadoestacheiocomenlatados", "aaaaaaaaa"),
    ("gatinhosadoraveisbrincandonaarea", "aa"),
    ("maratonadefilmescomecanasexta", "aaaaaaaa"),
    ("ciclismoeumodosustentaveldemover", "aaaaaaaaaaaa"),
    ("limpezageralnacasadoferiado", "aaaaa"),
    ("almocodedomingotemcarneassada", "aaaaaaaaaaaaaa"),
    ("bibliotecaspublicassaoessenciais", "aaaaaaaaaaaaa"),
    ("jogodotabuleiroestaquente", "aaaaaa"),
    ("musicasnovasestaoemtodasaslistas", "aaaaaaaaaaaaaaaaaaa"),
    ("comidarapidaepraticaeconveniente", "aaaaaaaaaaaaaaa"),
    ("cachorroslatemparaodesconhecidos", "aaaaaaaa"),
    ("domingodetempofamiliadiversao", "aaa"),
    ("acampamentonaserrafritanotemperatura", "aaaaaaaaaaaaaaaaaaaaaa"),
    ("estacoesdotremtemhorariosfixos", "aaaaa"),
    ("camisetacomdesenhododinofofa", "aaaaaaaaa"),
    ("sorvetedefrutassobremesaideal", "aaaaaaa"),
    ("roupasdeinvernosaoquentinhas", "aaaaaa"),
    ("florestasdensaosemprecombarulhos", "aaaaaaaaaa"),
    ("cadernoderecadosfoiencontrado", "aaaa"),
    ("macaeverdeebemsuave", "aaaa"),
    ("barcospesqueirossaomuitoativos", "aaaaaa"),
    ("bicicletaeumesmomeiotransporte", "aaaaaaaaaaaaa"),
    ("jardinagemetranquilizanteehrelaxante", "aaaaaaaaaaa"),
    ("livrosdeaventuraempolgantes", "aaaaaaaaaaaaaaa"),
    ("cafeteriasurbanassaocharmosas", "aaaaaaaaaaa"),
    ("mapasdetesourosdesenhadosempapel", "aaaaaaaaaa"),
    ("noitefriaechuvosaacendeolareira", "aaaaaaaaaaaaaaaaaaa"),
    ("avidadesemtrabalhoepaz", "aaaaa"),
    ("despertadortocoucedomadrugada", "aaaaaaaaaaaaaa"),
    ("planetasdouniversoparecemgigantes", "aaaaaaa"),
    ("estrelasbrilhantesnaceuazul", "aaaaaa"),
    ("museusguardamartefatosantigos", "aaa"),
    ("galaxiassaoimensasemisteriosas", "aaaaaaaaaaaaaaaaaaaaaaaaa"),
    ("caminhadaspelamontanhaesaoideais", "aaaaaaaaaaaaaaa"),
    ("temperaturacaiudepoisdochave", "aaaaa"),
    ("filmesdesuspensetiramofolego", "aaaaaaaa"),
    ("passarinhoscantamnofinaldatarde", "aaaaaaaaaaaaaaaaaaaa"),
    ("pianistaspraticamtodososdias", "aaaaa"),
    ("bolofofocomgostosodelimaoficadelicia", "aaa"),
    ("labirintosemfimdesafiajogadores", "aaaaaaaaa"),
    ("turistasadmiramacidadehistorica", "aaa"),
    ("meiascoloridassaoamadasporcriancas", "aaaaaaaa"),
    ("veraoechuvosoalaganovamente", "aaaaaaaaaaaaaaaaaa"),
    ("zezeviuazebra", "aaa"),
    ("socorro", "aaaaa"),
    ("socorro", "aa"),
    ("socorro", "a"),
    ("palmeiras", "aa"),
    ("palmeiras", "aaa"),
    ("quandosurgeoalviverdeimponentenogramadoemquealutaoaguardasabebemoquevempelafrentequeadurezadoprelionaotardaeopalmeirasnoardordapartidatransformandoalealdadeempadraosabesemprelevardevencidaemostrarquedefatoecampeaodefesaqueninguempassalinhaatacantederacatorcidaquecantaevibradefesaqueninguempassalinhaatacantederacatorcidaquecantaevibrapornossoalviverdeinteiroquesabeserbrasileiroostentandoasuafibra", "aaa"),
    ("quandosurgeoalviverdeimponentenogramadoemquealutaoaguardasabebemoquevempelafrentequeadurezadoprelionaotardaeopalmeirasnoardordapartidatransformandoalealdadeempadraosabesemprelevardevencidaemostrarquedefatoecampeaodefesaqueninguempassalinhaatacantederacatorcidaquecantaevibradefesaqueninguempassalinhaatacantederacatorcidaquecantaevibrapornossoalviverdeinteiroquesabeserbrasileiroostentandoasuafibra", "aaaaaa"),
    ("quandosurgeoalviverdeimponentenogramadoemquealutaoaguardasabebemoquevempelafrentequeadurezadoprelionaotardaeopalmeirasnoardordapartidatransformandoalealdadeempadraosabesemprelevardevencidaemostrarquedefatoecampeaodefesaqueninguempassalinhaatacantederacatorcidaquecantaevibradefesaqueninguempassalinhaatacantederacatorcidaquecantaevibrapornossoalviverdeinteiroquesabeserbrasileiroostentandoasuafibra", "aaaaaaaaaaaaaaa"),
    ("quaseninguemvequantomaisotempopassamaisaumentaagracaemvoceocoracaodisparatropecaquaseparaencaronoteubeijoqueaquimevejointeiroeuameitever", "aaaaaaaaaaaaaaaaaaaaaaaaaa"),
    ("anoticiaeumformatodedivulgacaodeumacontecimentopormeiosjornalisticoseamateriaprimadojornalismonormalmentereconhecidacomoalgumdadooueventosocialmenterelevantequemerecepublicacaoemummeiodecomunicacaosocialfatospoliticossociaiseconomicosculturaisnaturaiseoutrospodemsernoticiaseafetaremindividuosougrupossignificativosparaumdeterminadoveiculodeimprensaanoticiapodeserdefinidacomoumprodutosocialmenteconstruidopoiseresultadodasposicoessociaisdeindividuosegruposenvolvidoscomaproducaojornalisticaepelaspropriasfontesqueatuamcomodefinidoresprimariosdoseventosanoticiaeumacondensacaodessesdeterminantesemumprodutosocioculturalessencialnaconstrucaodosprocessosconteudoserelacoessociais", "aaaaaa"),
    ("anoticiaeumformatodedivulgacaodeumacontecimentopormeiosjornalisticoseamateriaprimadojornalismonormalmentereconhecidacomoalgumdadooueventosocialmenterelevantequemerecepublicacaoemummeiodecomunicacaosocialfatospoliticossociaiseconomicosculturaisnaturaiseoutrospodemsernoticiaseafetaremindividuosougrupossignificativosparaumdeterminadoveiculodeimprensaanoticiapodeserdefinidacomoumprodutosocialmenteconstruidopoiseresultadodasposicoessociaisdeindividuosegruposenvolvidoscomaproducaojornalisticaepelaspropriasfontesqueatuamcomodefinidoresprimariosdoseventosanoticiaeumacondensacaodessesdeterminantesemumprodutosocioculturalessencialnaconstrucaodosprocessosconteudoserelacoessociais", "aaaaaaa"),
    ("anoticiaeumformatodedivulgacaodeumacontecimentopormeiosjornalisticoseamateriaprimadojornalismonormalmentereconhecidacomoalgumdadooueventosocialmenterelevantequemerecepublicacaoemummeiodecomunicacaosocialfatospoliticossociaiseconomicosculturaisnaturaiseoutrospodemsernoticiaseafetaremindividuosougrupossignificativosparaumdeterminadoveiculodeimprensaanoticiapodeserdefinidacomoumprodutosocialmenteconstruidopoiseresultadodasposicoessociaisdeindividuosegruposenvolvidoscomaproducaojornalisticaepelaspropriasfontesqueatuamcomodefinidoresprimariosdoseventosanoticiaeumacondensacaodessesdeterminantesemumprodutosocioculturalessencialnaconstrucaodosprocessosconteudoserelacoessociais", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
])

def test_freq_dist_attack(texto_original, chave_correta):
    cifra = encrypt(texto_original, chave_correta)

    attempts = freq_dist_attack(cifra, testing=True)

    # verifica se o tamanho da chave correta está entre as tentativas
    assert len(chave_correta) in attempts
