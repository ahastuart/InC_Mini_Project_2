function redirectToInfoBoard(stationName) {
    // 역 이름을 URL 파라미터로 추가하여 info_board 페이지로 이동
    window.location.href = `/board?station=${encodeURIComponent(stationName)}`;
}