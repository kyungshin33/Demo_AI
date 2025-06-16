import os
from flask import Flask, render_template

app = Flask(__name__)

# 차트 자동 생성
def generate_chart():
    audio_dir = os.path.join(app.static_folder, 'audio', '100')
    image_dir = os.path.join(app.static_folder, 'images', '100')

    chart = []
    audio_files = sorted(f for f in os.listdir(audio_dir) if f.endswith('.m4a'))

    for idx, filename in enumerate(audio_files, start=1):
        song_id = os.path.splitext(filename)[0]
        image_path = os.path.join(image_dir, f"{song_id}.png")

        # 이미지 존재 확인
        if os.path.exists(image_path):
            chart.append({
                "id": song_id,
                "title": song_id,       # 임시로 파일명을 제목으로 사용
                "artist": "Unknown",    # 필요 시 별도 매핑
                "rank": idx
            })

    return chart

@app.route('/')
def index():
    chart = generate_chart()
    return render_template('chart.html', chart=chart)

if __name__ == '__main__':
    app.run(debug=True)
