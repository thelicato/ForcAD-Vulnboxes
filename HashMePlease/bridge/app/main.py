from app import create_app

app = create_app(debug=True)

def main() -> None:
    app.run()

if __name__ == "__main__":
    app.run()
