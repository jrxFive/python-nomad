import nomad
import warnings


def test_default_host_no_warning():
    warnings.simplefilter("always")

    with warnings.catch_warnings(record=True) as w:
        _ = nomad.Nomad()
        assert len(w) == 0


def test_address_default_host_warning_triggered():
    warnings.simplefilter("always")

    with warnings.catch_warnings(record=True) as w:
        _ = nomad.Nomad(address="http://localhost")
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)


def test_address_host_warning_triggered():
    warnings.simplefilter("always")

    with warnings.catch_warnings(record=True) as w:
        _ = nomad.Nomad(address="http://localhost", host="localhost")
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)


def test_address_default_host_muted_warning():
    warnings.simplefilter("ignore")

    with warnings.catch_warnings(record=True) as w:
        _ = nomad.Nomad(address="http://localhost")
        assert len(w) == 0
