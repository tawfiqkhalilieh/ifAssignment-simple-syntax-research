const app = () => {
  let x: number = 5;

  if ((x = 10)) {
    console.log("Hello");
  } else {
    console.log("No");
  }
};

app();
