from flask import Flask, send_file, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stack Overflow Technology Trends</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .chart-container {
            position: relative;
            height: 70vh;
            width: 100%;
            margin-top: 20px;
        }
        .info-panel {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 6px;
            font-size: 14px;
        }
        .info-panel h3 {
            margin-top: 0;
            color: #333;
        }
        .legend-custom {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }
        .legend-item {
            display: flex;
            align-items: center;
            padding: 5px 10px;
            background: #fff;
            border-radius: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            cursor: pointer;
            transition: all 0.2s;
        }
        .legend-item:hover {
            transform: translateY(-1px);
            box-shadow: 0 2px 5px rgba(0,0,0,0.15);
        }
        .legend-color {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 6px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="text-align: center; color: #333; margin-bottom: 30px;">Stack Overflow Technology Trends</h1>
        <div class="chart-container">
            <canvas id="myChart"></canvas>
        </div>
        <div class="info-panel">
            <h3>How to Use This Chart:</h3>
            <ul>
                <li>Hover over data points to see exact percentages and question counts</li>
                <li>Click on legend items to show/hide specific technologies</li>
                <li>Compare multiple technologies by looking at intersection points</li>
                <li>Use the percentage scale to understand relative popularity</li>
            </ul>
        </div>
    </div>
    <script src="/static/script.js"></script>
</body>
</html>
'''

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/<path:filename>')
def serve_data(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True) 
