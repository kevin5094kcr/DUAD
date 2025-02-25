import gui

def test_main_window():
    window = gui.show_main_window()
    assert window is not None
    window.close()