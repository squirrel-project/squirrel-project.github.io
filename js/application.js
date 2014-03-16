require.config({
    map: {
      '*': { 'jquery': 'jquery-private' },
      'jquery-private': { 'jquery': 'jquery' }
    },
    paths: {
        jquery:     'jquery-1.11.0.min',
        hbs: '../vendor/hbs/hbs',
        templates: '../templates/'
    }
    
});

require([ 'markup' ], function( markup ){
    markup.render()
});
