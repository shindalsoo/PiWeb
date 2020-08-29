// $$('.bbswrite-save').on('click', function(){
//   alert(1);
//   var formData = app.form.convertToData('#form-bbs-save');
//   alert(formData);
// });

function fBbsWriteSave (opt,id) {
  var formData = app.form.convertToData('#form-bbs-save');
	if (formData.category == '') {
		app.dialog.alert ('카테로기명을 입력하세요.', '입력오류');
	} else if (formData.word == '') {
		app.dialog.alert ('단어를 입력하세요.', '입력오류');
	} else {
		switch(opt){
			case 'insert':
				url = '/bbs_save_insert';break;
			case 'update':
				url = '/bbs_save_update/'+id;break;
		}
	    app.request.post (url, formData, function (data) {
    	console.log(data);
      	discoverView.router.back({force : true, ignoreCache : true, reload : true});
    });

    // app.request.post ('/bbs/insert', formData, function (data) {	
		// 	msg = JSON.parse (data);
		// 	if (msg.success) {
    //     fntoastTop ('gg');
    //     app.router.navigate('/bbs/list', {reloadCurrent:true})
    //     //app.router.back ({force : true, ignoreCache : true, reload : true});
		// 	} else if (! msg.success) {
		// 		app.dialog.alert (msg.failMsg, '저장오류');
		// 	} else {
		// 		app.dialog.alert ('예상치 않은 오류가 발생했습니다.', '기타오류');
		// 	}
		// });
	}
}