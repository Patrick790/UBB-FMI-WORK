class Item {
    constructor({ id, name, team, position, height, birthDate, isCaptain }) {
        this.id = id;
        this.name = name;
        this.team = team;
        this.position = position;
        this.height = height;
        this.birthDate = new Date(birthDate);
        this.isCaptain = isCaptain;
    }
}


function loadItems(jsonList) {
    const items = [];
    for (let i = 0; i < jsonList.length; i++) {
        items.push(new Item({
            id: jsonList[i].id,
            name: jsonList[i].name,
            team: jsonList[i].team,
            position: jsonList[i].position,
            height: jsonList[i].height,
            birthDate: new Date(jsonList[i].birthDate),
            isCaptain: jsonList[i].isCaptain
        }));
    }
    return items;
}

module.exports={ Item:Item, loadItems:loadItems };
