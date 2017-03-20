var app = new Vue({
  el: '#app',
  data: {
    url: '',
    movie: {}
  },
  methods: {
    getMovie: function(url) {
      var app = this;
      var imdb = url.split('title/')[1].split('/')[0];

      axios.get('/api/movie/get/' + imdb)
        .then(function (response) {
          var data = response.data;
          data.title = data.title.replace(/(.\d{4}.)/, ''); // fix (2017) in title
          data.release_date = data.release_date.replace(/\([^\)]*\)/, '').trim();
          data.iso_date = fix_date(data.release_date);
          app.movie = data;
        })
        .catch(function (error) {
          console.log(error);
      });

      app.url = '';
    },
    addMovie: function() {
      var movie = this.movie;

      axios.post('/api/movie/create/', {
        imdb_id: movie.imdb_id, // tt4425200
        title: movie.title, // John Wick: Chapter 2 (2017)
        photo: movie.photo, // https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_UX182_CR0,0,182,268_AL_.jpg
        year: movie.year, // 2017
        rated: movie.rated, // 14A
        runtime: movie.runtime,
        plot: movie.plot, // After returning to the criminal ...
        release_date: movie.release_date
      })
      .then(function (response) {
        var data = response.data;
        console.log(JSON.stringify(data));
      })
      .catch(function (error) {
        console.log(error);
      });
    },
  }
});

function fix_date(str) {
  // fix date string into ISO format
  var split = str.split(' ');
  var month = new Date(Date.parse(split[1] +" 1, 2012")).getMonth()+1;
  return split[2] + '-' + month + '-' + split[0];
}
