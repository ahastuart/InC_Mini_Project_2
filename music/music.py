from flask import Blueprint, jsonify, request
from music.spotify import getPlaylist as getTracks
from music.spotify import search as getPlaylist
from music.youtube import search as getYoutubeId

music_bp = Blueprint('music', __name__, url_prefix='/api/music')

@music_bp.route('/', methods=['GET'])
def get_playlist():
    try:
        emotion = request.args.get('emotion')
        keyword = request.args.get('keyword') 
        playlist_id = getPlaylist.main(emotion=emotion, keyword=keyword)
        track_list = getTracks.main(playlist_id)
        
        video_info_list = []

        for track in track_list[:3]:
            video_info = getYoutubeId.main(track)
            video_info_list.append({
                'track': track,
                'video_id': video_info[0]['videoId']
            })
        
        return jsonify({
            "videos": video_info_list
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500