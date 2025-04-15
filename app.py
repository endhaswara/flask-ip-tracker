from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    print(f"[LOG] IP: {ip_address}, User-Agent: {user_agent}")

    return f"""
        <h1>Halo!</h1>
        <p><strong>IP kamu:</strong> {ip_address}</p>
        <p><strong>User Agent:</strong> {user_agent}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
