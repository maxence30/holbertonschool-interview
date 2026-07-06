#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  function printCharacters (index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], function (err, res, characterBody) {
      if (err) {
        return;
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);
      printCharacters(index + 1);
    });
  }

  printCharacters(0);
});
