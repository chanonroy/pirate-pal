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
    }
  }
});
