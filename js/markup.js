define([ 
    'jquery',
    'hbs!templates/header',
    'hbs!templates/footer'
], function( $, headerTpl, footerTpl ){
    var render = function render(){
        var body   = $( 'body '),
            klass  = body.attr( 'class' ),
            header = $( headerTpl()),
            footer = $( footerTpl());

        klass = klass ? klass.split( ' ' ) : [];
        for( var i=0; i<klass.length; i++ ){
            if( klass[ i ])
                header.find( 'li.' + klass[ i ]).addClass( 'active' );
        }
        body.prepend( header );
        body.append( footer );
    };
    return {
        render: function(){ $( document ).ready( render )}
    }
});
