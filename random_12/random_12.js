(function() {
    const myQuestions = [
      {
        question: "Ab",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "A",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "Bb",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "Bb",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "C",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "Db",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "D",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "Eb",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "E",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "F",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "Gb",
        answers: {
        },
        correctAnswer: "a"
      },
      {
        question: "G",
        answers: {
        },
        correctAnswer: "a"
      }
    ];
  
    function buildQuiz() {
      // we'll need a place to store the HTML output
      const output = [];
      const QuestionList = myQuestions.sort(() => Math.random() - .5)
  
      // for each question...
      QuestionList.forEach((currentQuestion, questionNumber) => {
        // we'll want to store the list of answer choices
        const answers = [];
  
        // and for each available answer...
        for (letter in currentQuestion.answers) {
          // ...add an HTML radio button
          answers.push(
            `<label>
               <input type="radio" name="question${questionNumber}" value="${letter}">
                ${letter} :
                ${currentQuestion.answers[letter]}
             </label>`
          );
        }
  
        // add this question and its answers to the output
        output.push(
          `<div class="slide">
             <div class="question"> ${currentQuestion.question} </div>
             <div class="answers"> ${answers.join("")} </div>
           </div>`
        );
      });
  
      // finally combine our output list into one string of HTML and put it on the page
      quizContainer.innerHTML = output.join("");
    }
  
    function showResults() {
      // gather answer containers from our quiz
      const answerContainers = quizContainer.querySelectorAll(".answers");
  
      // keep track of user's answers
      let numCorrect = 0;
  
      // for each question...
      myQuestions.forEach((currentQuestion, questionNumber) => {
        // find selected answer
        const answerContainer = answerContainers[questionNumber];
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;
  
        // if answer is correct
        if (userAnswer === currentQuestion.correctAnswer) {
          // add to the number of correct answers
          numCorrect++;
  
          // color the answers green
          answerContainers[questionNumber].style.color = "lightgreen";
        } else {
          // if answer is wrong or blank
          // color the answers red
          answerContainers[questionNumber].style.color = "red";
        }
      });
  
      // show number of correct answers out of total
      resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}`;
    }
  
    function showSlide(n) {
      slides[currentSlide].classList.remove("active-slide");
      slides[n].classList.add("active-slide");
      currentSlide = n;
      

      
      if (currentSlide === slides.length - 1) {
        nextButton.style.display = "none";

      } else {
        nextButton.style.display = "inline-block";

      }
    }
  
    function showNextSlide() {
      showSlide(currentSlide + 1);
    }
  

  
    const quizContainer = document.getElementById("quiz");
    const resultsContainer = document.getElementById("results");

  
    // display quiz right away
    buildQuiz();
  
    const nextButton = document.getElementById("next");
    const slides = document.querySelectorAll(".slide");
    let currentSlide = 0;
  
    showSlide(0);
  
    // on submit, show results

    nextButton.addEventListener("click", showNextSlide);
  })();