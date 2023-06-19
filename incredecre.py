var createCounter = function(init) {
    let counter = init;
  
    return {
        increment: function() {
            return ++counter;
        },
        reset: function() {
            counter = init;
            return counter;
        },
        decrement: function() {
            return --counter;
        }
    };
};

const counter = createCounter(5);
console.log(counter.increment()); // Output: 6
console.log(counter.reset()); // Output: 5
console.log(counter.decrement()); // Output: 4
