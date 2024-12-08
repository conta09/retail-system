import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
    QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class SupermarketScanner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supermarket Scanner")
        self.setGeometry(100, 100, 900, 600)
        self.initUI()

    def initUI(self):
        # Main container
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Apply modern styles using QSS
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QLabel#HeaderLabel {
                background-color: #007bff;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QLabel#FooterLabel {
                color: #6c757d;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 5px;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QHeaderView::section {
                background-color: #007bff;
                color: white;
                padding: 5px;
                font-weight: bold;
                border: none;
            }
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)

        # Header Label
        header_label = QLabel("Supermarket Scanner")
        header_label.setObjectName("HeaderLabel")
        header_label.setFont(QFont("Arial", 18, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)

        # Table to display scanned products
        self.table = QTableWidget(0, 3)  # Rows, Columns
        self.table.setHorizontalHeaderLabels(["Product", "Price", "Quantity"])
        self.table.horizontalHeader().setStretchLastSection(True)
        main_layout.addWidget(self.table)

        # Total and Buttons Section
        bottom_layout = QHBoxLayout()

        # Total Label
        self.total_label = QLabel("Total: $0.00")
        self.total_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.total_label.setAlignment(Qt.AlignLeft)
        bottom_layout.addWidget(self.total_label)

        # Clear Button
        clear_button = QPushButton("Clear All")
        clear_button.clicked.connect(self.clear_table)
        bottom_layout.addWidget(clear_button)

        # Add bottom layout to the main layout
        main_layout.addLayout(bottom_layout)

        # Footer Label
        footer_label = QLabel("Designed for Quick Scanning & Offline Use")
        footer_label.setObjectName("FooterLabel")
        footer_label.setFont(QFont("Arial", 10, QFont.StyleItalic))
        footer_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(footer_label)

    def add_product(self, product_name, price, quantity):
        """
        Adds a product to the table.
        """
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(product_name))
        self.table.setItem(row_count, 1, QTableWidgetItem(f"${price:.2f}"))
        self.table.setItem(row_count, 2, QTableWidgetItem(str(quantity)))

        # Update total
        current_total = float(self.total_label.text().split("$")[1])
        new_total = current_total + (price * quantity)
        self.total_label.setText(f"Total: ${new_total:.2f}")

    def clear_table(self):
        """
        Clears the table and resets the total.
        """
        self.table.setRowCount(0)
        self.total_label.setText("Total: $0.00")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SupermarketScanner()
    window.show()

    # Add some demo products
    window.add_product("Milk", 2.5, 2)
    window.add_product("Bread", 1.2, 1)

    sys.exit(app.exec_())
