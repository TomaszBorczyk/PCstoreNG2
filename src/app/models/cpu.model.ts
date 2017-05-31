import { ProductModel } from './product/product.model'

export class CpuModel extends ProductModel{
  watts:number;
  frequency:number;
  cache:number;
  core:number;
  socket:string;
}
