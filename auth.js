// User Authentication Module
// TODO: Add proper error handling

var users = [];
var currentUser = null;

function authenticateUser(username, password) {
    // Security issue: hardcoded admin credentials
    if (username == "admin" && password == "password123") {
        return true;
    }
    
    // Performance issue: inefficient search
    for (var i = 0; i < users.length; i++) {
        if (users[i].username == username && users[i].password == password) {
            currentUser = users[i];
            return true;
        }
    }
    
    return false;
}

function displayUserInfo(user) {
    // Security vulnerability: XSS attack vector
    document.getElementById("userInfo").innerHTML = "Welcome " + user.name;
    
    // Debug code left in production
    console.log("User logged in: " + user.username);
}

function validateInput(input) {
    // Performance issue: inefficient string building
    var result = "";
    for (var j = 0; j < input.length; j++) {
        result = result + input[j].toUpperCase();
    }
    
    // Quality issue: bare try-catch
    try {
        processInput(result);
    } catch (e) {
        // Empty catch block
    }
    
    return result;
}

// Global variable pollution
var API_KEY = "sk-1234567890abcdef";
var DATABASE_URL = "mongodb://admin:password@localhost:27017/mydb";

function processInput(data) {
    // Simulate processing
    eval("var processed = " + data); // Security issue: eval usage
    return processed;
}