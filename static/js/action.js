function GetCookies(key) {
  // Получаем значение с document.cookie по 'key'
  var getFullCookieJSON = document.cookie.match(new RegExp("(?:^|; )"+key.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
  // если null, тогда создаем пустой массив
  if (getFullCookieJSON == null) {
    var arrFilms = [];
  }
  // иначе если доступный, тогда конвертируем JSON в массив
  else {
    var arrFilmsJSON = getFullCookieJSON[1];
    var arrFilms = JSON.parse(arrFilmsJSON);
  }
  console.log('Get: ' +arrFilms);
  return arrFilms;
}


// принимаем на вход массивФильмов, youtubeID, дни существования куков
function SetCookies(arrFilms, youtubeID, days) {
  arrFilms.unshift(youtubeID);           // добавляем youtubeID в начало массива
  var setCookie = JSON.stringify(arrFilms);   // конвертируем массив у JSON
  document.cookie = 'Products='+setCookie+';path=/;max-age=(60*60*24*'+days+')';     // устанавливаем куки на количество days
  console.log('Set: ' + setCookie);
}


var newArrProducts = GetCookies('Products');
$('.add_to_basket').on('click', function() {

  // получаем mongo _id у товара
  var mongoId = $(this).attr('id');
  SetCookies(newArrProducts, mongoId, 7);
  console.log(mongoId);
});
