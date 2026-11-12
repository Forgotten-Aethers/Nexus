import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView

frontend = Path(__file__).parent
basedir = frontend.parent

app = QApplication(sys.argv)

window = QWebEngineView()
window.setWindowTitle("Nexus")
window.setWindowIcon(QIcon(str(basedir / "assets" / "images" / "Icosaedro-Nexus-logo.ico")))
window.showMaximized()
window.setMinimumSize(400, 400)

html = frontend / "html" / "index.html"
window.load(html.as_uri())

window.show()

sys.exit(app.exec())