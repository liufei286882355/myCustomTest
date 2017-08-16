//
//  LFTableViewDatasource.m
//  LFTextView
//
//  Created by 刘飞 on 2017/8/16.
//  Copyright © 2017年 刘飞. All rights reserved.
//

#import "LFTableViewDatasource.h"

@interface LFTableViewDatasource ()

@property (nonatomic, strong) NSArray *itemsArray;
@property (nonatomic, copy) NSString *cellIdentifier;
@property (nonatomic, copy) TableViewCellConfigureBlock configureCellBlock;

@end


@implementation LFTableViewDatasource


-(id)init {
    return nil;
}

-(id)initWithItems:(NSArray *)itemsArray cellIdentifier:(NSString *)identifier configureCellBlock:(TableViewCellConfigureBlock)aConfigureCellBlock {
    
    self = [super init];
    if (self) {
        self.itemsArray = itemsArray;
        self.cellIdentifier = identifier;
        self.configureCellBlock = [aConfigureCellBlock copy];
    }
    return self;
}

-(id)itemAtIndexPath:(NSIndexPath *)indexPath {
    return self.itemsArray[(NSUInteger) indexPath.row];
}


#pragma mark UITableViewDataSource

-(NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return self.itemsArray.count;
}

-(UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:self.cellIdentifier forIndexPath:indexPath];
    
    id item = [self itemAtIndexPath:indexPath];
    self.configureCellBlock(cell, item);
    return cell;
}

@end
