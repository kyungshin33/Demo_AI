from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def chart():
    audio_folder = os.path.join(app.static_folder, 'audio', '100')
    image_folder = os.path.join(app.static_folder, 'images', '100')

    # 오디오와 이미지 파일 목록 정렬
    audio_files = sorted([f for f in os.listdir(audio_folder) if f.endswith('.m4a')])
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.png')])

    songs = []
    for idx, audio_file in enumerate(audio_files):
        title = os.path.splitext(audio_file)[0]
        artist = "unknown"  # 필요시 mutagen 등으로 추출 가능

        # 이미지 파일이 부족한 경우를 대비해 조건 체크
        image_file = image_files[idx] if idx < len(image_files) else 'default.png'

        songs.append({
            'rank': idx + 1,
            'title': title,
            'artist': artist,
            'audio': url_for('static', filename=f'audio/100/{audio_file}'),
            'thumbnail': url_for('static', filename=f'images/100/{image_file}'),
            'rank_change': 1 if idx % 2 == 0 else -1  # 예시로 오르내림 설정
        })

    return render_template('chart.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)