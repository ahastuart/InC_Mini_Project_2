window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple, {
            labels: {
                placeholder: "검색...", // 검색 입력란 플레이스홀더
                perPage: "개로 정렬", // 페이지당 항목 수
                noRows: "표시할 항목이 없습니다.", // 항목이 없을 때 메시지
                info: "" 
            }
        });
    }
});
