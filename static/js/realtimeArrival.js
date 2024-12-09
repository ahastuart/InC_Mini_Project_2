// 실시간지하철 정보 관련 함수들

//실시간 지하철 정보 가져오기, 역 이름이 다를 경우 앞의 두 글자 검색으로 진행
function fetchRealtimeArrival(stationName) {
    const simplifiedStationName = stationName.replace(/\(.*?\)/g, '');
    fetch(`/api/realtimeArrival?stationName=${encodeURIComponent(simplifiedStationName)}`)
        .then(response => response.json())
        .then(data => {
            if (data.error || (data.realtimeArrivalList && data.realtimeArrivalList.length === 0)) {
                console.warn('정확한 역 이름이 일치하지 않음. 두 글자로 재시도합니다.');
                const stationQuery = simplifiedStationName.slice(0, 2);

                return fetch(`/api/realtimeArrival?stationName=${encodeURIComponent(stationQuery)}`)
                    .then(response => response.json())
                    .then(retryData => {
                        if (retryData.error || (retryData.realtimeArrivalList && retryData.realtimeArrivalList.length === 0)) {
                            console.error('두 글자 검색으로도 역 정보를 찾을 수 없습니다.');
                            displayErrorInfo('역 정보를 찾을 수 없습니다.');
                        } else {
                            displayRealtimeInfo(retryData, stationName);
                        }
                    })
                    .catch(error => console.error('두 글자 요청 실패:', error));
            } else {
                displayRealtimeInfo(data, stationName);
            }
        })
        .catch(error => console.error('실시간 도착 정보 가져오기 오류:', error));
}

// 오류 정보를 표시하는 함수
function displayErrorInfo(message) {
    const infoContainer = document.getElementById('realtime-info');
    infoContainer.innerHTML = `<p class="text-danger">${message}</p>`;
}

// 실시간 도착 정보를 HTML에 표시하는 함수
function displayRealtimeInfo(data, stationName) {
    const infoContainer = document.getElementById('realtime-info');
    infoContainer.innerHTML = `<h3><strong>${stationName}역</strong></h3>`;

    if (data.error) {
        infoContainer.innerHTML += `<p class="text-danger">${data.error}</p>`;
    } else {
        const arrivals = data.realtimeArrivalList || [];
        
        arrivals.forEach(arrival => {
            const arrivalStatus = getArrivalStatus(arrival.arvlCd);
            const trainType = arrival.btrainSttus;
            const arrivalTimeInSeconds = arrival.barvlDt;
            const remainingTime = arrivalTimeInSeconds ? `약 ${arrivalTimeInSeconds}초` : "정보 없음";
            const arrivalMessage = arrival.arvlMsg2;
            const trainLine = arrival.trainLineNm;
            
            infoContainer.innerHTML += `
                <div class="arrival-info card">
                    <div class="card-body">
                        <h5 class="card-title">${trainLine}</h5>
                        <p class="card-text">
                            <strong><span class="arrival-status ${arrivalStatus.class}">${arrivalStatus.text}</span></strong> - ${arrivalMessage}
                            <br>열차 종류: ${trainType}
                            <br>남은 시간: ${remainingTime}
                        </p>
                    </div>
                </div>`;
        });
    }
}

// 도착 코드에 따른 상태 반환 함수
function getArrivalStatus(arvlCd) {
    switch (arvlCd) {
        case "0": return { text: "진입 중", class: "status-entering" };
        case "1": return { text: "도착", class: "status-arrived" };
        case "2": return { text: "출발", class: "status-departed" };
        case "3": return { text: "전역 출발", class: "status-prev-departed" };
        case "4": return { text: "전역 진입", class: "status-prev-entering" };
        case "5": return { text: "전역 도착", class: "status-prev-arrived" };
        case "99": return { text: "운행 중", class: "status-running" };
        default: return { text: "정보 없음", class: "status-unknown" };
    }
}
