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
          console.log(JSON.stringify(data));
          app.movie = data;
        })
        .catch(function (error) {
          console.log(error);
      });

      app.url = '';
    },
    createMovie: function() {
      var app = this;

      axios.post('/api/movie/create/', {
        imdb_id: app.imdb_id,
        title: app.title,
        photo: app.photo,
        year: app.year,
        rated: app.rated,
        runtime: app.runtime,
        plot: app.plot,
        release_date: app.release_date
      })
      .then(function (response) {
        var data = response.data;
        console.log(JSON.stringify(data));
      })
      .catch(function (error) {
        console.log(error);
      });

    }
  }
});
