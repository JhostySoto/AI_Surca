from surca_ai.constantes import AVISO_SIMULADO, SEMANAS_A_ESTIMAR


def test_estimamos_dos_semanas():
    assert SEMANAS_A_ESTIMAR == 2


def test_aviso_de_datos_simulados():
    assert "simulados" in AVISO_SIMULADO
