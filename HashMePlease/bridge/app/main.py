from app import create_app

app = create_app(debug=True)

def main() -> None:
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
