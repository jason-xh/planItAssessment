// TASK
/*
Challenge 6:
Make an API call to https://petstore.swagger.io/v2/pet/findByStatus?status=available and display a count of
the number of pets in the result
*/
// note that I believe node does not currently come with fetch

const uniquePets = new Map();

fetch('https://petstore.swagger.io/v2/pet/findByStatus?status=available')
    .then(response => response.json())
    .then(data => {
        // this bit here utilises a map to track unique pets, not sure if this is necessary
        // or if the data given is bad?
        data.forEach(pet => {
            if (!uniquePets.has(pet.id)) {
                uniquePets.set(pet.id, pet);
            }
        });
        console.log("# of pets: " + data.length)
        console.log("# of unique pets: " + uniquePets.size);
    });

// OUTPUT

// # of pets: 425
// # of unique pets: 29
