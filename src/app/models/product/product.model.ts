export class ProductModel{
  id:number;
  name:string;
  uuid:string;
  category:string;
  brand:string;
  amount:number;
  totalRating:number;
  price:number;

  constructor(id:number,
              name:string,
              uuid:string,
              category:string,
              brand:string,
              amount:number,
              totalRating:number,
              price:number){
    this.id=id;
    this.name=name;
    this.uuid=uuid;
    this.category=category;
    this.brand=brand;
    this.amount=amount;
    this.totalRating=totalRating;
    this.price=price;
  }

}
