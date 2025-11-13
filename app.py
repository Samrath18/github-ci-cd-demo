def add(a, b):
    return a + b

def generate_html(result):
    html_content = f"""
    <html>
      <head><title>GitHub CI/CD Demo</title></head>
      <body style='font-family:Arial; text-align:center; margin-top:50px;'>
        <h1>🚀 GitHub CI/CD Demo</h1>
        <p>The result of add(2, 3) is: <strong>{result}</strong></p>
        <p>✅ Build and deployment were successful!</p>
      </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    result = add(2, 3)
    print(f"The result is {result}")
    generate_html(result)
