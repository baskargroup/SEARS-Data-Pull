

/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('dope');

// Insert a few documents into the sales collection.
db.getCollection('productData').updateMany(
    {}, [
    {
    $set: {
      solvents: {
        $map: {
          input: "$solvents",
          as: "solvent",
          in: {
            name: "$$solvent.name",
            value: "$$solvent.value",
            mol_wt: "", // Replace with actual value or keep empty if not available
            smiles: "", // Replace with actual value or keep empty if not available
            hsp_delta_d: 0, // Replace with actual value or keep as 0
            hsp_delta_p: 0, // Replace with actual value or keep as 0
            hsp_delta_h: 0  // Replace with actual value or keep as 0
          }
        }
      }
    }
  }
]
);