// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
});

$("#datatablesSimple").DataTable({
  // 스크롤바 설정
  scrollX: true,
  scrollY: 200,

  // 열 넓이 설정
  columnDefs: [
      // 2번째 항목 넓이를 100px로 설정
      { targets: 0, width: 250 },
      { targets: 1, width: 250 },
      { targets: 2, width: 250 },
      { targets: 3, width: 250 },
      { targets: 4, width: 250 },
      { targets: 5, width: 250 }
  ]
});
