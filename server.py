from asyncore import write
from crypt import methods
from flask import Flask, request
from file_read_backwards import FileReadBackwards


app = Flask(__name__)

@app.route('/add/<topic>', methods=["POST"])
def add(topic):
    content = request.get_json()
    with open('./history.txt', 'a') as file:
        temp = topic + " - " + content["value"] + " " + content["timestamp"] + "\n"
        file.write(temp)
        # file.close()
    return '''Hello'''

# @app.route('/results/<topic>', methods=["GET"])
# def result(topic):
#     pass
    
@app.route('/results/<topic>/<history>', methods=["GET"])
def result_with_history(topic, history:str='1'):
    history = int(history)
    temp = ""
    with FileReadBackwards('./history.txt', encoding="utf-8") as frb:
        for i in range(history):
            line = frb.readline()
            temp += line
            if not line:
                break
    return temp

    


if __name__ == "__main__":
    app.run(debug=True)
