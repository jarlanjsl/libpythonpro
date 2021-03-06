import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['silvajarlan@gmail.com', 'jarlan.silva@sodine.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'vitoria.lima1994@gmail.com',
        'Cursos Python Pro',
        'Aula da turma Henrique Bastos',
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'jarlan.silva']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'vitoria.lima1994@gmail.com',
            'Cursos Python Pro',
            'Aula da turma Henrique Bastos',
        )
