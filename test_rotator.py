import pytest


@pytest.fixture(autouse=True)
def mock_talon(mocker):
    mocker.patch("talon.app", return_value=mocker.MagicMock())
    mocker.patch("talon.actions", return_value=mocker.MagicMock())
    mocker.patch("talon.actions.user", return_value=mocker.MagicMock())
    mocker.patch("talon.actions.edit", return_value=mocker.MagicMock())
    mocker.patch("talon.actions.edit.select_all", return_value=mocker.MagicMock())


HOMOPHONES = {
    "world": ["world", "whirled", "whorled"],
    "whirled": ["whirled", "world", "whorled"],
    "whorled": ["whorled", "whirled", "world"],
}
CANONICAL_HOMOPHONE = "world"


def test_rotate(mocker):
    import talon

    from .rotator import Actions

    # TODO: use pytest parametrization
    for current, rotated in [
        [
            "look at the whirled",
            "look at the world",
        ],
        [
            "look at the world",
            "look at the whirled",
        ],
    ]:
        mocker.patch("talon.actions.edit.selected_text", return_value=current)
        mocker.patch("talon.actions.user.homophones_get_all", return_value=HOMOPHONES)
        spy = mocker.spy(talon.actions.user, "paste")
        Actions.rotate_word(CANONICAL_HOMOPHONE)
        spy.assert_called_once_with(rotated)
