var input = document.getElementById("guess");
        var table = document.getElementById("table");
        var word = "{{word.word}}"

        input.addEventListener("keypress", function(event) {
          if (event.key === "Enter") {
            // Prevent refrehsing the page?
            event.preventDefault();
            
            // Insert a new row into the table
            var row = table.insertRow(0);
            var cell1 = row.insertCell(0);

            // Make string to place in new row
            var colored = "";
            let split = input.value.toLowerCase().split("");
            let word_split = word.toLowerCase().split("");

            // If guessed word == word
            if (input.value.toLowerCase() == word.toLowerCase()) {
                cell1.innerHTML = "<span style='color: #61c961'>" + input.value + "</span>";
                swal({
                    title: "Correct!",
                    text: "You guessed the artist. Play again?",
                    buttons: {
                        cancel: {
                            text: "No",
                            value: null,
                            visible: true
                        },
                        confirm: {
                            text: "Yes!",
                            value: true
                        }
                    }
                    })
                    .then((playAgain) => {
                    if (playAgain) {
                        location.reload();
                    } else {
                        ;
                    }
                    });
            }
            
            // Otherwise color text
            for (let i = 0; i < split.length; i++) {
                if (split[i] == word_split[i]) {
                    colored += "<span style='color: #61c961'>" + split[i] + "</span>";
                } else if (word_split.slice(word_split.indexOf(split[i])).includes(split[i])){
                    colored +=  "<span style='color: #ffff57'>" + split[i] + "</span>";
                } else {
                    colored += split[i];
                }
            }
            cell1.innerHTML = colored;
            
            // Reset input field to blank
            input.value = "";
          }
        });