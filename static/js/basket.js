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
  var ageCookie = 60*60*24*days
  console.log(ageCookie)

  document.cookie = 'Products='+setCookie+';path=/;max-age='+ageCookie;     // устанавливаем куки на количество days
  console.log('Set: ' + setCookie);
}

var newArrProducts = GetCookies('Products');
$('.delete_basket').on('click', function() {
    SetCookies([], 0, 0)
    console.log('Deleted all shop items in basket');
});