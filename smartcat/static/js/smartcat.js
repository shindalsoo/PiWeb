function fBbs_Save_Insert () {
  	var formData = app.form.convertToData('#form-bbs-save');
	if (formData.category == '') {
		app.dialog.alert ('카테고리명을 입력하세요.', '입력오류');
	} else if (formData.word == '') {
		app.dialog.alert ('단어를 입력하세요.', '입력오류');
	} else {
		app.request.post ('/bbs_save_insert', formData, function (data) {
			console.log(data);
			//fntoastTop ('gg');
			//app.router.navigate('/bbs/list', {reloadCurrent:true})
			discoverView.router.back({force : true, ignoreCache : true, reload : true});
		});
	}
}
function fBbs_Save_Update (id) {
	var formData = app.form.convertToData('#form-bbs-save');
	if (formData.category == '') {
		app.dialog.alert ('카테고리명을 입력하세요.', '입력오류');
	} else if (formData.word == '') {
		app.dialog.alert ('단어를 입력하세요.', '입력오류');
	} else {
		app.request.post ('/bbs_save_update/'+id, formData, function (data) {
			console.log(data);
			//fntoastTop ('gg');
			//app.router.navigate('/bbs/list', {reloadCurrent:true})
			discoverView.router.back({force : true, ignoreCache : true, reload : true});
		});
  }
}
function fBbs_Save_Delete (id) {
	app.dialog.confirm ('정말로 삭제하시겠습니까 ?','삭제확인',function(){
		var formData = app.form.convertToData('#form-bbs-save');
		app.request.post ('/bbs_save_delete/'+id, formData, function (data) {
			console.log(data);
			//fntoastTop ('gg');
			//app.router.navigate('/bbs/list', {reloadCurrent:true})
			discoverView.router.back({force : true, ignoreCache : true, reload : true});
		});

	});
}