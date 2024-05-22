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

function GetHtmlToInsert(urlImg, title, description, measure, price){
    var htmlText = '<div class="item_in_basket_list display_flex"><div class="left_flex"><img class="item_img_in_basket_list" src="'+urlImg+'"><div class="item_title_and_description_in_basket_list"><div class="item_title_in_basket_list shop_item_title">'+title+'</div><div class="item_description_in_basket_list">'+description+'</div></div></div><div class="item_price_and_measure_in_basket_list"><div class="item_measure_in_basket_list">Кол-во: 1 '+measure+'</div><div class="item_price_in_basket_list">'+price+' ₽</div></div></div>';
    return htmlText;
}

var newArrProducts = GetCookies('Products');
console.log(newArrProducts);

var mainHtmlText = '';
newArrProducts.forEach(function(item, i, newArrProducts) {
    fetch("api/shop/item/" + item)
      .then(async (response) => {
        let data = await response.json();


        document.getElementById('basket_list').innerHTML ='<div>html data</div>';
        mainHtmlText += GetHtmlToInsert(data.photo_url, data.itemName, data.description, data.measure, data.price)
        document.getElementById('basket_list').innerHTML = mainHtmlText;
      });
});

$('.delete_basket').on('click', function() {
    SetCookies([], 0, 0)
    console.log('Deleted all shop items in basket');
    location.reload()
});

function makeOrderFromBasket(){
    console.log('Make order');
    var IdUser = document.getElementById('id_username').value;
    var IdPhone = document.getElementById('id_phone').value;
    var IdAddress = document.getElementById('id_address').value;

    fetch('api/order', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(
            {
                username: IdUser,
                phone: IdPhone,
                address: IdAddress,
                products: GetCookies('Products')
            }
        )
    })
    SetCookies([], 0, 0);
    location.reload()
    return false;
}