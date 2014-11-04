'use strict';
var gulp = require('gulp');
var gutil = require('gulp-util');
// sass
var sass = require('gulp-sass');
// sourcemaps
var sourcemaps = require('gulp-sourcemaps');
// livereload
var livereload = require('gulp-livereload');

// --------------------------
// SASS (dev)
// --------------------------
gulp.task('sass', function() {
  return gulp.src('./client/scss/*.scss')
    .pipe(sourcemaps.init())
    .pipe(sass())
    // error logging
    .on('error', gutil.log)
    // write sourcemaps to a specific directory
    .pipe(sourcemaps.write('./'))
    // give it a file and save
    .pipe(gulp.dest('./static/css'));
});


// --------------------------
// DEV/WATCH TASK
// --------------------------
gulp.task('watch', ['sass'], function() {
  livereload.listen(35729, function(err){
    gutil.log(gutil.colors.bgGreen('... Listening on 35729...'));
    if (err) {
      return console.log(err);
    }
  });

  gulp.watch('./static/css/**/*.css').on('change', function(event) {
    gutil.log(gutil.colors.bgBlue('Reloading css...'));
    livereload.changed(event.path);
  });

  // watch the sources and rebuild
  gulp.watch('./client/scss/**/*.scss', ['sass']);

  gutil.log(gutil.colors.bgGreen('Watching for changes...'));
});

// build task
gulp.task('build', [
  'sass'
]);

gulp.task('default', ['watch']);
