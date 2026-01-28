// Load plugins
const gulp = require("gulp");

// Copy third party libraries from /node_modules into /vendor
gulp.task('vendor', function(cb) {
  // Font Awesome
  gulp.src([
      './node_modules/@fortawesome/**/*',
    ])
    .pipe(gulp.dest('./assets/vendor'))

  // Trackswitch
  gulp.src([
      './node_modules/trackswitch/dist/**/*',
  ])
  .pipe(gulp.dest('./assets/vendor/trackswitch'))

  // Lazyload
  gulp.src([
    './node_modules/lazyload/lazyload.min.js',
    './node_modules/lazyload/lazyload.js'
  ])
  .pipe(gulp.dest('./assets/vendor/lazyload'))

  cb();

});

gulp.task("default", gulp.parallel('vendor'));
