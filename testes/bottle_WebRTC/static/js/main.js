'use strict';

navigator.getUserMedia = navigator.getUserMedia ||
    navigator.webkitGetUserMedia || navigator.mozGetUserMedia;

var constraints = {
  audio: false,
  video: true
};
var video_box = null;

function successCallback(stream) {
  window.stream = stream; // stream available to console  
  if (window.URL) {
    video_box.src = window.URL.createObjectURL(stream);
  } else {
    video_box.src = stream;
  }
}

function errorCallback(error) {
  console.log('navigator.getUserMedia error: ', error);
}

function getMedia(video_box){
	video_box = document.querySelector(video_box);
	navigator.getUserMedia(constraints, successCallback, errorCallback);
}
