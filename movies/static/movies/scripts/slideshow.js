var slideIndexRear = 0;
var slideIndexFront = 2;
var SLIDES_COUNT = 3;
var currentSlides= ["","",""];
var slidesSrc = [];
var i;

function setSlides(slides)
{
    slidesSrc= slides;
    for(i=0; i < SLIDES_COUNT ; i++)
		    currentSlides[i] = slidesSrc[(slideIndexRear+i) % slidesSrc.length];
    showSlides();

}

function plusSlides(n)
{
	 	var i;

		if(n > 0)
		{
			  for(i = SLIDES_COUNT-1; i >0;i--)
				    currentSlides[i] = currentSlides[i-1];
			  slideIndexRear= (slideIndexRear - 1 + slidesSrc.length) %slidesSrc.length;
			  slideIndexFront= (slideIndexFront - 1 + slidesSrc.length) %slidesSrc.length;
			  currentSlides[i] = slidesSrc[slideIndexRear];
			  
		}
		else{
			  for(i = 0; i < SLIDES_COUNT-1;i++)
				    currentSlides[i] = currentSlides[i+1];
			  slideIndexRear = (slideIndexRear + 1) %slidesSrc.length;
			  slideIndexFront = (slideIndexFront + 1) %slidesSrc.length;
			  currentSlides[i] = slidesSrc[slideIndexFront];
		}
		
	  showSlides();
}

function showSlides() {
	  var i;
	  var slides = document.getElementsByClassName("cover-photo");

	  for(i = 0; i < SLIDES_COUNT ; i ++)
	  	  slides[i].src = currentSlides[i] ;  
}
