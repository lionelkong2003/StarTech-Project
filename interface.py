import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Long-term Burn-in Display Anomaly Detector")
        self.resize(900, 600)

        container = QWidget(self)
        layout = QVBoxLayout(container)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(24)

        title = QLabel("Initialized Successfully", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: 600;")

        image_label = QLabel(self)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        image_path = "Software Initial Image.jpg"  # 项目根目录下的图片
        pixmap = QPixmap(image_path)
        
        scaled = pixmap.scaledToWidth(480, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled)

        # 用缩小到 1x1 的方式取整张图的平均色
        avg_color = (
            pixmap.toImage()
            .scaled(1, 1, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
            .pixelColor(0, 0)
        )
        bg_color = f"#{avg_color.red():02x}{avg_color.green():02x}{avg_color.blue():02x}"

        layout.addWidget(title)
        layout.addWidget(image_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)

        container.setStyleSheet(f"background-color: {bg_color};")
        self.setCentralWidget(container)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
