var slideIndexRear = 0;
var slideIndexFront = 2;
var SLIDES_COUNT = 3;
var currentSlides= ["","",""];
var slidesSrc = [];
var slides_id = [];
var current_ids = [];
var i;

function setSlides(slides,ids)
{
    slidesSrc= slides;
    slides_id = ids;
    for(i=0; i < SLIDES_COUNT ; i++)
    {
		  	    currentSlides[i] = slidesSrc[(slideIndexRear+i) % slidesSrc.length];
		  	    current_ids[i] = slides_id[(slideIndexRear+i) % slidesSrc.length];
	}
    showSlides();

}

function plusSlides(n)
{
	 	var i;

		if(n > 0)
		{
			  for(i = SLIDES_COUNT-1; i >0;i--)
				    {
				    currentSlides[i] = currentSlides[i-1];
				    current_ids[i] = current_ids[i -1];
				    }
			  slideIndexRear= (slideIndexRear - 1 + slidesSrc.length) %slidesSrc.length;
			  slideIndexFront= (slideIndexFront - 1 + slidesSrc.length) %slidesSrc.length;
			  currentSlides[i] = slidesSrc[slideIndexRear];
			  current_ids[i] = slides_id[slideIndexRear];
		}
		else{
			  for(i = 0; i < SLIDES_COUNT-1;i++)
				    {
				    currentSlides[i] = currentSlides[i+1];
				    current_ids[i] = current_ids[i+1];
				    }
			  slideIndexRear = (slideIndexRear + 1) %slidesSrc.length;
			  slideIndexFront = (slideIndexFront + 1) %slidesSrc.length;
			  currentSlides[i] = slidesSrc[slideIndexFront];
			  current_ids[i] = slides_id[slideIndexFront];
		}
		
	  showSlides();
}

function showSlides() {
	  var i;
	  var slides = document.getElementsByClassName("cover-photo");

	  for(i = 0; i < SLIDES_COUNT ; i ++)
	  {
	  	  slides[i].src = currentSlides[i] ;
	  	  slides[i].parentNode.href = "movie/" + current_ids[i];
	  	 }
}
